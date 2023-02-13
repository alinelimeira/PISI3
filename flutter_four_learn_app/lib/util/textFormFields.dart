import 'package:flutter/material.dart';

class OutlinedTextFormField extends StatefulWidget {
  final TextEditingController controller;
  final bool enableSuggestions;
  final bool autocorrect;
  final String? hintText;
  final bool isDense;
  final Icon? icon;
  final FormFieldValidator<String>? validator;
  final TextInputType? keyboardType;
  final bool obscureText;
  const OutlinedTextFormField({
    Key? key,
    required this.controller,
    this.enableSuggestions = false,
    this.autocorrect = false,
    this.hintText,
    this.isDense = true,
    this.icon,
    this.validator,
    this.keyboardType,
    this.obscureText = false,
  }) : super(key: key);

  @override
  State<OutlinedTextFormField> createState() => _OutlinedTextFormFieldState();
}

class _OutlinedTextFormFieldState extends State<OutlinedTextFormField> {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration:
          BoxDecoration(border: Border.all(width: 1, color: Colors.grey)),
      child: TextFormField(
        controller: widget.controller,
        enableSuggestions: widget.enableSuggestions,
        autocorrect: widget.autocorrect,
        keyboardType: widget.keyboardType,
        obscureText: widget.obscureText,
        decoration: InputDecoration(
            border: InputBorder.none,
            hintText: widget.hintText,
            isDense: widget.isDense,
            icon: widget.icon),
        validator: widget.validator,
      ),
    );
  }
}
