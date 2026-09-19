@echo off
cd /d G:\ProgramData\Obisidian_Notes\Obsidian_Notes
if "%1"=="pull" (
    git pull origin master
    if errorlevel 1 (echo Pull failed) else (echo Pull completed!)
) else if "%1"=="push" (
        for /f "delims=" %%a in ("git status --porcelain") do set HAS=1
        if defined HAS (
            set /p MSG="Commit message [Enter=auto]: "
            if "%MSG%"=="" set MSG=Auto sync
            git add -A
            git commit -m "%MSG%"
            if errorlevel 1 (echo Commit failed.& pause& exit)
        ) else (echo No changes to commit.)
        echo Pushing...
        git push origin master
        if errorlevel 1 (echo Push failed) else (echo Push completed!)
    ) else (
        git status
        git log --oneline -5
    )
)
pause
