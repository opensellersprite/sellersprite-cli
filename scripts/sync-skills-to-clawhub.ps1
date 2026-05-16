#!/usr/bin/env pwsh
# Sync src/sellersprite_cli/skills/ to the standalone sellersprite-skills repo for ClawHub.
#
# Prereqs:
#   1. Create the empty public repo on GitHub first:
#        https://github.com/opensellersprite/sellersprite-skills
#   2. Ensure the working tree is clean (commit or stash first).
#
# Usage:
#   ./scripts/sync-skills-to-clawhub.ps1                # push to master
#   ./scripts/sync-skills-to-clawhub.ps1 -Branch main   # push to main
#   ./scripts/sync-skills-to-clawhub.ps1 -DryRun        # preview only
#
# Re-run after each skills change. ClawHub picks up the new version automatically
# (bump `version:` in skills/SKILL.md beforehand).

param(
    [string]$RemoteUrl = "https://github.com/opensellersprite/sellersprite-skills.git",
    [string]$Branch    = "master",
    [string]$Prefix    = "src/sellersprite_cli/skills",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

# Resolve repo root from script location
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $RepoRoot

Write-Host "==> Repo root  : $RepoRoot"
Write-Host "==> Prefix     : $Prefix"
Write-Host "==> Remote     : $RemoteUrl"
Write-Host "==> Branch     : $Branch"

# 1. Sanity: prefix must exist and contain SKILL.md
$SkillMd = Join-Path $RepoRoot "$Prefix/SKILL.md"
if (-not (Test-Path $SkillMd)) {
    throw "SKILL.md not found at $SkillMd"
}

# 2. Sanity: working tree must be clean (subtree push refuses dirty trees in some setups)
$dirty = git status --porcelain
if ($dirty) {
    Write-Host "`n[!] Working tree has uncommitted changes:" -ForegroundColor Yellow
    Write-Host $dirty
    throw "Commit or stash before running subtree push."
}

# 3. Show the version that will be pushed
$frontmatter = Get-Content $SkillMd -TotalCount 10 | Out-String
if ($frontmatter -match 'version:\s*(\S+)') {
    Write-Host "==> SKILL.md version: $($Matches[1])"
} else {
    Write-Host "[!] No version field detected in SKILL.md frontmatter" -ForegroundColor Yellow
}

if ($DryRun) {
    Write-Host "`n[DryRun] Would run:"
    Write-Host "  git subtree push --prefix=$Prefix $RemoteUrl $Branch"
    return
}

# 4. Push the skills subtree to the standalone repo
Write-Host "`n==> Pushing subtree..."
git subtree push --prefix=$Prefix $RemoteUrl $Branch
if ($LASTEXITCODE -ne 0) {
    throw "git subtree push failed with exit code $LASTEXITCODE"
}

Write-Host "`n[OK] Subtree pushed to $RemoteUrl ($Branch)" -ForegroundColor Green
Write-Host "Next: visit https://clawhub.ai to refresh the skill listing if it doesn't auto-update."
