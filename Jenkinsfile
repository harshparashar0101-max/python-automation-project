pipeline {
    agent any
    stages {
        stage('Check Environment') {
            steps {
                bat '"C:\\Users\\ADMIN\\AppData\\Local\\Python\\bin\\python.exe" --version'
            }
        }
        stage('Run Calculator Tests') {
            steps {
                dir('C:\\Users\\ADMIN\\Desktop\\New folder\\VC1\\jenkins-project') {
                    bat '"C:\\Users\\ADMIN\\AppData\\Local\\Python\\bin\\python.exe" test_calculator.py'
                }
            }
        }
        stage('Run Jira export') {
            steps {
                dir('C:\\Users\\ADMIN\\Desktop\\New folder\\VC1\\jenkins-project') {
                    bat 'chcp 65001 && "C:\\Users\\ADMIN\\AppData\\Local\\Python\\bin\\python.exe" Jira_export.py'
                }
            }
        }

        stage('Update Jira') {
            steps {
                jiraComment(
                    issueKey: 'LOGI-7',
                    body: 'Jenkins build completed successfully! All stages passed.'
                )
            }
            
        stage('Done') {
            steps {
                echo 'All stages completed successfully!'
            }
        }
    }
}