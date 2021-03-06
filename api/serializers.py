from rest_framework import serializers

from api.models import Apar, InspectionReport, PressureReport, UserAccessLevel, VerificationReport

class UserAccessLevelSerializer (serializers.ModelSerializer):
    class Meta:
        model  = UserAccessLevel
        fields = '__all__'

class AparSerializer (serializers.ModelSerializer):
    inspeksi = serializers.ReadOnlyField (source = 'inspeksi.inspection.id')
    
    class Meta:
        model  = Apar
        fields = '__all__'

class InspectionReportSerializer (serializers.ModelSerializer):
    apar = serializers.ReadOnlyField (source = 'apar.identifier')
    aparid = serializers.ReadOnlyField (source = 'apar.id')
    inspector = serializers.ReadOnlyField (source = 'inspector.username')
    verification = serializers.ReadOnlyField (source = 'verificationid')
    
    class Meta:
        model  = InspectionReport
        fields = '__all__'

class VerificationReportSerializer (serializers.ModelSerializer):
    class Meta:
        model  = VerificationReport
        fields = '__all__'

class PressureReportSerializer (serializers.ModelSerializer):
    class Meta:
        model  = PressureReport
        fields = '__all__'
