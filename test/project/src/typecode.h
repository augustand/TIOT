#ifndef TYPECODE_H
#define TYPECODE_H

/* I2C 传感器属性 */
typedef struct {
	unsigned char  State;
	unsigned short Type;		//传感器类型
	unsigned short Unit;		//传感器数据单位
	float value;	//数值
} SensorRegValue;	

/* the code for sensor state */
/* bit0 of State: Power down? 1: Power On 0:Power down */
/* bit1 of State: connettion error 1: connecttion ok 0: error */

/* the code for sensor type */
#define SENSOR_UserData	0x0000	//用户自定义数据
#define SENSOR_Temp		0x0001	//温度
#define SENSOR_Humid		0x0002	//湿度
#define SENSOR_GAS		0x0003	//可燃气体
#define SENSOR_V		0x0004	//电压
#define SENSOR_Cur		0x0005	//电流
#define SENSOR_Freq		0x0006	//频率
#define SENSOR_Light		0x0007  //照度
#define SENSOR_Pressure		0x0008	//压强
#define SENSOR_Switch		0x0009	//开关量:( (1000+Hz)*当前状态)  ,紫外
#define SENSOR_WaterGage	0x000A	//水位
#define SENSOR_Rainfall		0x000B	//降水总量
#define SENSOR_Resistence	0x000C	//电阻
#define SENSOR_Timer		0x000D	//时间周期
#define SENSOR_ERR			0x000E	//错误的物理量编码
#define SENSOR_Concentration 0x000F //浓度
#define SENSOR_PH			0x0010	//PH值
#define SENSOR_smog			0x0011	//烟雾


/* the code for the unit of value */
#define UNIT_NULL		0x0000	//无单位
#define UNIT_TempC		0x0001	//摄氏度
#define UNIT_Perc		0x0002	//百分比
#define UNIT_V			0x0003	//伏
#define UNIT_A			0x0004	//安
#define	UNIT_Hz			0x0005	//Hz
#define UNIT_Pa			0x0006	//帕
#define UNIT_KPa		0x0007	//千帕
#define UNIT_MA			0x0008	//毫安
#define UNIT_Lumen		0x0009	//流明
#define UNIT_Centimetre	0x000A	//厘米
#define UNIT_Millimetre	0x000B	//毫米
#define UNIT_UserDefine 0x000C 	//用户自定义的表达方式
#define UNIT_Ohm		0x000D	//欧姆
#define UNIT_Lux		0x000E	//勒克司（Lux）
#define UNIT_Sec		0x000F	//秒
#define UNIT_ERR		0x0010	//错误的单位编码
#define UNIT_MgPerL		0x0011	//毫克每升
#define UNIT_Switch   0x0012  //开关量单位

#define UNIT_Switch   0x0012  //开关量单位
extern char* Physical[];

#endif
