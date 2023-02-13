import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter_four_learn_app/util/textButtons.dart';
import 'package:flutter_four_learn_app/util/textFormFields.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({Key? key}) : super(key: key);

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  late final TextEditingController _name;
  late final TextEditingController _email;
  late final TextEditingController _password;
  late final TextEditingController _telefone;
  late final TextEditingController _passwordcheck;
  final _formKey = GlobalKey<FormState>();

  @override
  void initState() {
    _name = TextEditingController();
    _email = TextEditingController();
    _password = TextEditingController();
    _telefone = TextEditingController();
    _passwordcheck = TextEditingController();
    super.initState();
  }

  @override
  void dispose() {
    _name.dispose();
    _email.dispose();
    _password.dispose();
    _telefone.dispose();
    _passwordcheck.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Scaffold(
        backgroundColor: Colors.white,
        body: Form(
          key: _formKey,
          child: SingleChildScrollView(
            // Implementa uma rolagem na tela
            child: SizedBox(
              height: size.height,
              width: size.width,
              child: Stack(
                children: [
                  Column(
                    children: [
                      Expanded(
                        child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Image.asset('assets/images/4learnLogo.png'),
                            ]),
                      ),

                      // CAMPOS DE CADASTRO DE USUÁRIO
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 30,
                          vertical: 30,
                        ),
                        decoration: const BoxDecoration(
                          color: Colors.white,
                          //borderRadius: BorderRadius.vertical(top: Radius.circular(45))
                        ),
                        child: Column(
                          children: [
                            //Nome do USUÁRIO
                            Padding(
                              padding: const EdgeInsets.only(bottom: 15),
                              child: OutlinedTextFormField(
                                controller: _name,
                                enableSuggestions: false,
                                autocorrect: false,
                                hintText: 'Nome',
                                isDense: true,
                                icon: Icon(Icons.person_outline),
                                validator: (val) {
                                  if (val == null) {
                                    return 'campo obrigatório';
                                  }
                                },
                              ),
                            ),
                            //EMAIL user@email.com
                            Padding(
                              padding: const EdgeInsets.only(bottom: 15),
                              child: OutlinedTextFormField(
                                controller: _email,
                                enableSuggestions: false,
                                autocorrect: false,
                                keyboardType: TextInputType.emailAddress,
                                hintText: 'Email',
                                isDense: true,
                                icon: Icon(Icons.email_outlined),
                                validator: (val) {
                                  if (val == null) {
                                    return 'Campo obrigatório';
                                  }
                                },
                              ),
                            ),

                            //SENHA ********
                            Padding(
                              padding: const EdgeInsets.only(bottom: 15),
                              child: OutlinedTextFormField(
                                controller: _password,
                                obscureText: true,
                                enableSuggestions: false,
                                autocorrect: false,
                                hintText: 'Senha',
                                isDense: true,
                                icon: Icon(Icons.lock_outline),
                                validator: (val) {
                                  if (val == null) {
                                    return 'Campo obrigatório';
                                  }
                                },
                              ),
                            ),

                            //Confirmar SENHA ********
                            Padding(
                              padding: EdgeInsets.only(bottom: 15),
                              child: OutlinedTextFormField(
                                controller: _passwordcheck,
                                obscureText: true,
                                enableSuggestions: false,
                                autocorrect: false,
                                hintText: 'Confirmar senha',
                                isDense: true,
                                icon: Icon(Icons.lock_outline),
                                validator: (val) {
                                  if (val == null) {
                                    return 'Campo obrigatório';
                                  }
                                  if (val != _password.text) {
                                    return 'Senhas não coincidem';
                                  }
                                  return null;
                                },
                              ),
                            ),

                            // TELEFONE (00) 00000-0000
                            Padding(
                              padding: const EdgeInsets.only(bottom: 15),
                              child: OutlinedTextFormField(
                                controller: _telefone,
                                enableSuggestions: false,
                                autocorrect: false,
                                hintText: 'Telefone',
                                isDense: true,
                                icon: Icon(Icons.phone_outlined),
                                validator: (val) {
                                  if (val == null) {
                                    return 'Campo obrigatório';
                                  }
                                },
                              ),
                            ),

                            // CADASRTRAR
                            SizedBox(
                                height: 45,
                                child: PrimaryOutlinedButton(
                                  title: 'CADASTRAR',
                                  onPressed: () async {
                                    final name = _name.text;
                                    final email = _email.text;
                                    final password = _password.text;
                                    final telefone = _telefone.text;
                                    if (_formKey.currentState!.validate()) {
                                      ScaffoldMessenger.of(context)
                                          .showSnackBar(
                                        const SnackBar(
                                            content: Text('Processing Data')),
                                      );
                                    }
                                    try {
                                      final UserCredential = await FirebaseAuth
                                          .instance
                                          .createUserWithEmailAndPassword(
                                              email: email, password: password);
                                    } on FirebaseAuthException catch (e) {
                                      if (e.code == 'weak password') {
                                        print('weak password');
                                      } else if (e.code ==
                                          'email-already-in-use') {
                                        print('email already in use');
                                      } else if (e.code == 'invalid-email') {
                                        print('invalid email');
                                      }
                                    }
                                    final user =
                                        FirebaseAuth.instance.currentUser;
                                    await user?.sendEmailVerification();
                                    await FirebaseFirestore.instance
                                        .collection("users")
                                        .doc(FirebaseAuth
                                            .instance.currentUser?.uid)
                                        .set({
                                      'uid': name,
                                      'email': email,
                                      'telefone': telefone,
                                    });
                                    Navigator.of(context).pushNamed('/');
                                  },
                                ))
                          ],
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ));
  }
}
