# Asset Management System

A comprehensive software solution designed to streamline tracking, monitoring, and management of organizational assets across buildings, floors, and rooms.

![Asset Management System Flow](https://github.com/tejeshx37/Asset-Managment-System/blob/main/Frontend/Flow_Diagram.jpg)

## Overview

This Asset Management System helps organizations effectively track, monitor, and manage their physical assets such as projectors, computers, and other equipment. The system optimizes asset utilization and maintenance through systematic data organization and analysis, providing actionable insights to support decision-making processes.

## System Architecture

The Asset Management System consists of four primary modules:

### User Management Module
- **Profile**: Manage user profiles and personal information
- **Authentication**: Secure login and access control
- **Authorization**: Role-based permissions and access rights

### Configuration Module
- **Building**: Manage building information and locations
- **Floor**: Define and manage floors within buildings
- **Room**: Configure rooms within floors
- **Asset**: Define asset types and categories

### Transaction Module
- **In-Ward**: Track asset acquisition and entry into the system
- **Damage**: Record and manage damaged assets and maintenance

### Report Module
- **360 Abstract Report**: Comprehensive overview of all assets
- **Asset Cost Abstract Report**: Financial analysis and reporting

## Key Features

- **Asset Tracking**: Real-time monitoring of asset location, status, and assignment
- **Maintenance Scheduling**: Track and schedule regular maintenance for assets
- **Visual Reports**: Data visualization with matplotlib for asset utilization trends
- **User-friendly Interface**: Built with Tkinter for intuitive user experience
- **Notification System**: Alert system implemented with tkMessageBox
- **Database Management**: Efficient storage and retrieval of asset information

## Technologies Used

- **Python**: Core programming language
- **Tkinter**: GUI framework
- **MySQL**: Database management
- **matplotlib**: Data visualization
- **tkMessageBox**: User notifications and alerts

## System Requirements

- Windows 10
- Python 3.x
- MySQL Server

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/asset-management-system.git
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure MySQL database:
   ```
   mysql -u root -p < database/setup.sql
   ```

4. Update database configuration in `config.py`

5. Run the application:
   ```
   python main.py
   ```

## Usage

1. **Login**: Enter your credentials to access the system
2. **Dashboard**: View overall asset statistics and important notifications
3. **Asset Management**: Add, edit, or remove assets from the system
4. **Reports**: Generate various reports on asset utilization and status
5. **Maintenance**: Schedule and track asset maintenance


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
