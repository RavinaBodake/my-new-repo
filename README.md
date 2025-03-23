parameters {
    string(name: 'testUrl', defaultValue: 'https://youtube.com', description: 'Enter the URL to test')
    choice(name: 'browser', choices: ['chrome', 'firefox'], description: 'Select the browser for testing')
    string(name: 'driversPath', defaultValue: 'C:\\Users\\pradn\\Downloads\\drivers', description: 'Enter the path to the drivers')
}

stages {
    stage('Checkout') {
        steps {
            git branch: 'main', url: 'https://github.com/RavinaBodake/exp-7.git'
        }
    }

    stage('Build') {
        steps {
            dir('selenium-tests') {
                bat 'mvn clean package -DdriversPath=%driversPath%'
            }
        }
    }

    stage('Test') {
        steps {
            dir('selenium-tests') {
                bat 'mvn test -DtestUrl=%testUrl% -Dbrowser=%browser% -DdriversPath=%driversPath%'
            }
        }
    }

    stage('Report') {
        steps {
            dir('selenium-tests') {
                bat 'allure generate --clean && allure open'
            }
        }
    }
}

post {
    success {
        echo 'Pipeline executed successfully!'
    }
    failure {
        echo 'Pipeline execution failed!'
    }
}
