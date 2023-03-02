import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class StandardTextField extends StatefulWidget {
  final String title;
  final Color color;
  final Color textColor;
  final double fontSize;
  final Widget? child;
  const StandardTextField(
      {this.title = '',
      this.color = const Color(0xFF44CDEB),
      this.textColor = Colors.black,
      this.fontSize = 16,
      this.child,
      super.key});

  @override
  State<StandardTextField> createState() => _StandardTextFieldState();
}

class _StandardTextFieldState extends State<StandardTextField> {
  @override
  Widget build(BuildContext context) {
    return Container(
      width: 292,
      height: 121,
      decoration: BoxDecoration(
        color: widget.color,
        borderRadius: BorderRadius.circular(10),
      ),
      child: Text(
        widget.title,
        textAlign: TextAlign.center,
        style: TextStyle(fontSize: widget.fontSize),
      ),
    );
  }
}
