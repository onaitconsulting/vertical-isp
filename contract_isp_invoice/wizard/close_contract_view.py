<?xml version="1.0" encoding="utf-8"?>
<openerp>
    <data>
        <record id="view_close_contract" model="ir.ui.view">
            <field name="name">A</field>
            <field name="model">contract.service.activate</field>
            <field name="arch" type="xml">
                <form string="Activate Service" version="7.0">
		    <group>
			<field name="activation_date" />
			<field name="account_id" invisible="1" />
			<field name="service_id" invisible="1" />
		    </group>
		    <footer>
			<button 
			    name="activate"
			    string="Activate"
			    type="object"
			    class="oe_highlight" />
			<button
			    string="Cancel"
			    class="oe_link"
			    special="cancel" />
		    </footer>
		</form>
	    </field>
	</record>
        <record id="action_view_contract_service_activate" model="ir.actions.act_window">
            <field name="name">Activate Service</field>
            <field name="type">ir.actions.act_window</field>
	    <field name="src_model">contract.service</field>
            <field name="res_model">contract.service.activate</field>
            <field name="view_type">form</field>
            <field name="view_mode">form</field>
	    <field name="context">{'default_service_id': active_id}</field>
            <field name="target">new</field>
        </record>

    </data>
</openerp>
