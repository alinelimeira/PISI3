import 'package:flutter_four_learn_app/src/LoginScreen.dart';
import 'package:flutter/material.dart';
import 'src/FirebaseAuth.dart';
import 'src/RegisterScreen.dart';
import 'firebase_options.dart';
import 'package:firebase_core/firebase_core.dart';
import 'src/mainScreen.dart';

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
        initialRoute: '/firebaseAuth',
        routes: {
          '/': (context) => LoginScreen(),
          '/FirebaseAuth': (context) => const FirebaseAuth(),
          '/Register': (context) => const RegisterScreen(),
          '/MainScreen': (context) => const MainScreen()
        });
  }
}
