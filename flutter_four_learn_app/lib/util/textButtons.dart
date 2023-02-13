import 'package:flutter/material.dart';

class PrimaryOutlinedButton extends StatefulWidget {
  final String title;
  final Color color;
  final Color textColor;
  final Function() onPressed;
  final BorderRadius? borderRadius;
  const PrimaryOutlinedButton(
      {Key? key,
      required this.title,
      this.color = Colors.greenAccent,
      this.textColor = const Color(0xFF00b894),
      required this.onPressed,
      this.borderRadius})
      : super(key: key);

  @override
  State<PrimaryOutlinedButton> createState() => _PrimaryOutlinedButtonState();
}

class _PrimaryOutlinedButtonState extends State<PrimaryOutlinedButton> {
  late final BorderRadius borderRadius;

  @override
  void initState() {
    super.initState();
    borderRadius = widget.borderRadius ?? BorderRadius.circular(8);
  }

  @override
  Widget build(BuildContext context) {
    return OutlinedButton(
      onPressed: widget.onPressed,
      child: Text(
        widget.title,
        style: TextStyle(
            color: widget.textColor, fontSize: 16, fontWeight: FontWeight.bold),
      ),
      style: OutlinedButton.styleFrom(
          minimumSize: Size.fromWidth(160),
          padding: EdgeInsets.all(6),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          side: BorderSide(color: widget.color, width: 2)),
    );
  }
}
