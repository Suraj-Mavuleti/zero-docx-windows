import sys
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, Pango

class ZeroDocx(Gtk.Window):
    def __init__(self):
        super().__init__(title="Zero Docx - Ultimate Studio")
        self.set_default_size(1100, 850)
        
        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.props.title = ""
        self.header.get_style_context().add_class("hidden-header")
        self.set_titlebar(self.header)
        
        self.setup_css()
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_box)
        
        # ================= RIBBON =================
        ribbon = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        ribbon.get_style_context().add_class("ribbon")
        main_box.pack_start(ribbon, False, False, 0)
        
        logo = Gtk.Label(label="Z E R O D O C X")
        logo.get_style_context().add_class("sidebar-logo")
        logo.set_margin_start(20)
        logo.set_margin_end(30)
        ribbon.pack_start(logo, False, False, 0)
        
        tools_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        tools_box.set_valign(Gtk.Align.CENTER)
        
        # Formatting buttons
        for icon in ["𝐁", "𝐼", "𝐔", "🔗", "🖼️", "📊"]:
            btn = Gtk.Button(label=icon)
            btn.get_style_context().add_class("format-btn")
            tools_box.pack_start(btn, False, False, 0)
            
        sep = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        sep.set_margin_start(10)
        sep.set_margin_end(10)
        tools_box.pack_start(sep, False, False, 0)
        
        for align in ["⬅️", "↔️", "➡️", "🔃"]:
            btn = Gtk.Button(label=align)
            btn.get_style_context().add_class("format-btn")
            tools_box.pack_start(btn, False, False, 0)
            
        ribbon.pack_start(tools_box, False, False, 0)
        
        btn_export = Gtk.Button(label="📥 Export PDF")
        btn_export.get_style_context().add_class("action-btn")
        btn_export.set_valign(Gtk.Align.CENTER)
        btn_export.set_margin_end(20)
        ribbon.pack_end(btn_export, False, False, 0)
        
        # ================= EDITOR WORKSPACE =================
        workspace = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        workspace.get_style_context().add_class("workspace-bg")
        main_box.pack_start(workspace, True, True, 0)
        
        # Scrollable area
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        workspace.pack_start(scroll, True, True, 0)
        
        # Centered paper wrapper
        paper_align = Gtk.Alignment.new(0.5, 0.0, 0, 1)
        paper_align.set_padding(40, 40, 0, 0)
        scroll.add(paper_align)
        
        self.paper = Gtk.TextView()
        self.paper.get_style_context().add_class("paper")
        self.paper.set_size_request(850, 1100)
        self.paper.set_wrap_mode(Gtk.WrapMode.WORD)
        self.paper.set_left_margin(80)
        self.paper.set_right_margin(80)
        self.paper.set_top_margin(80)
        self.paper.set_bottom_margin(80)
        self.paper.modify_font(Pango.FontDescription('Times New Roman 14'))
        
        self.paper.get_buffer().set_text(
            "Ultimate Studio Business Proposal\n\n"
            "Date: September 2026\n"
            "Author: Studio Team\n\n"
            "1. Executive Summary\n"
            "The integration of glassmorphism across all core applications has led to a 400% increase in user retention. "
            "Our secure architecture ensures privacy without compromising aesthetics.\n\n"
            "2. Objectives\n"
            "- Finalize the Docx implementation.\n"
            "- Prepare for full suite deployment.\n\n"
            "This document is a placeholder demonstrating the premium zero-docx engine."
        )
        
        paper_align.add(self.paper)
        
    def setup_css(self):
        css = b'''
            window { background-color: #030305; }
            .hidden-header { background: #030305; min-height: 0px; padding: 0px; border: none; box-shadow: none; }
            .ribbon { background-color: rgba(10, 12, 18, 0.98); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 15px 0px; }
            .sidebar-logo { color: #FFFFFF; font-size: 20px; font-weight: 900; letter-spacing: 5px; text-shadow: 0 0 15px rgba(0, 153, 255, 0.6); }
            .format-btn { background: transparent; color: #FFFFFF; border: 1px solid transparent; border-radius: 8px; font-size: 16px; padding: 8px 12px; transition: all 0.2s ease; }
            .format-btn:hover { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); }
            .action-btn { background: linear-gradient(45deg, #0099FF, #0055FF); color: #FFFFFF; border-radius: 12px; font-weight: bold; padding: 8px 15px; border: none; box-shadow: 0 5px 15px rgba(0, 153, 255, 0.3); transition: all 0.3s; }
            .action-btn:hover { box-shadow: 0 8px 25px rgba(0, 153, 255, 0.5); }
            .workspace-bg { background: #050608; }
            .paper { background-color: #FFFFFF; color: #000000; box-shadow: 0 15px 50px rgba(0,0,0,0.8); border-radius: 4px; line-height: 1.8; caret-color: #000000; }
            .paper text { background-color: #FFFFFF; }
        '''
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    win = ZeroDocx()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
