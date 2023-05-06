import 'package:flutter_four_learn_app/src/FomularioScreen.dart';
import 'package:flutter_four_learn_app/src/LoginScreen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_four_learn_app/src/PomodoroListScreen.dart';
import 'package:flutter_four_learn_app/src/ProfileScreen.dart';
import 'package:flutter_four_learn_app/src/StudyTime.dart';
import 'src/FirebaseAuthentication.dart';
import 'src/RegisterScreen.dart';
import 'firebase_options.dart';
import 'package:firebase_core/firebase_core.dart';
import 'src/BottonNavigation.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const FourLearnApp());
}

class FourLearnApp extends StatelessWidget {
  const FourLearnApp({Key? key}) : super(key: key);

  // This widget is the root of our application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blueGrey,
        ),
        debugShowCheckedModeBanner: false,

        //Definindo rotas no APP
        initialRoute: '/',
        routes: {
          '/': (context) => const LoginScreen(),
          '/FirebaseAuth': (context) => const FirebaseAuthenticatio(),
          '/Register': (context) => const RegisterScreen(),
          '/MainScreen': (context) => const MainScreen(),
          '/ProfileScreen': (context) => const ProfileScreen(),
          '/FormularioScreen': (context) => const FormularioScreen(),
          '/PomodoroListScreen': (context) => const PomodoroListScreen(),
          '/StudyTimeScreen': (context) => const StudyTime()
        });
  }
}
