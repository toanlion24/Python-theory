# Script to push to GitHub without Quiz 05 Answers file
# Run this script from PowerShell outside of Cursor IDE

cd "d:\Python\Theory"

Write-Host "Removing git lock file..." -ForegroundColor Yellow
if (Test-Path ".git\index.lock") { 
    Remove-Item ".git\index.lock" -Force
    Start-Sleep -Seconds 1
}

Write-Host "Removing Answers file from git tracking..." -ForegroundColor Yellow
git rm --cached "Phase_1_Python Fundamentals/Python_Quiz_05/Python_Quiz_05_Answers.ipynb" 2>&1 | Out-Null

Write-Host "Adding files to git..." -ForegroundColor Yellow
git add .gitignore
git add "Phase_1_Python Fundamentals/"
git add "Phase_2_Data Structures & File Handling/"
git add "Phase_3_Object-Oriented Programming & Modules/"
git add "Data Structures & Algorithms/"
git add "Python_Developer_Roadmap.md"
git add "requirements.txt"

# Remove deleted files from Learn the Basics
git add -u "Learn the Basics/"

Write-Host "`nChecking status..." -ForegroundColor Yellow
git status --short | Select-String "Quiz_05"

Write-Host "`nCommitting changes..." -ForegroundColor Yellow
git commit -m "Add Phase 1-3, Quiz 05 (without answers), Data Structures & Algorithms"

Write-Host "`nPushing to GitHub..." -ForegroundColor Yellow
git push origin main

Write-Host "`nDone!" -ForegroundColor Green
