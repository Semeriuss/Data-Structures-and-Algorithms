from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.minlen = float("inf")
        
        prefixsum = [0]
        for i, num in enumerate(nums):
            prefixsum.append(prefixsum[i] + num)
        
        def findMinSub(sp, ep, arr, k, dp):
            if (sp, ep) in dp: return dp[(sp, ep)]
            if sp > ep or ep < 0 or ep >= len(arr) or sp < 0 or sp >= len(arr):
                dp[(sp, ep)] = -1
                return 
            
            if arr[ep] - arr[sp] >= k:
                dp[(sp, ep)] = ep - sp
                self.minlen = min(self.minlen, ep - sp)
            
            dp[(sp, ep)] = findMinSub(sp + 1, ep, arr, k, dp)
            dp[(sp, ep)] = findMinSub(sp, ep - 1, arr, k, dp)
            
        
        findMinSub(0, len(prefixsum) - 1, prefixsum, k, {})

        return self.minlen if self.minlen != float("inf") else -1

""" 
[1]
1
[1,2]
4
[2,-1,2]
3
[-490,-84,-242,756,579,290,232,545,869,-274,565,207,-115,380,951,849,-253,532,54,678,195,477,478,220,714,488,252,-165,21,405,440,944,927,-82,903,-260,252,168,415,-266,269,226,3,599,-370,-453,-436,-487,99,793,359,692,-24,832,203,529,-80,882,863,-440,-181,-455,922,389,-432,974,-438,-404,990,565,237,-135,782,486,344,422,658,185,722,253,439,475,279,682,-103,540,536,727,109,422,-9,-306,546,-410,143,975,-326,693,105,965,75,376,476,-90,-414,-419,938,-418,692,827,824,33,-452,688,572,252,170,147,29,218,954,112,28,745,-11,697,931,-142,-304,201,523,568,-230,73,-281,949,-135,-445,424,-212,864,116,937,-50,276,-15,874,825,-115,761,791,591,364,876,881,968,747,162,531,342,117,363,815,21,-49,317,514,-17,379,806,129,200,57,-380,-202,-188,41,488,861,119,892,514,506,951,134,-324,-105,555,8,-422,864,-100,-94,-493,434,360,-154,-428,-73,322,446,-474,389,883,254,-444,399,535,-327,-33,749,534,29,656,578,-452,387,496,370,429,399,708,973,-463,897,661,132,153,152,97,-23,-269,-474,-469,510,402,168,832,-161,-359,337,989,414,393,934,349,-208,-321,188,309,789,732,465,669,-85,362,-167,292,718,415,531,137,-30,-373,607,151,-118,-459,102,541,-234,687,242,-167,472,150,895,-439,742,703,-359,520,399,733,671,999,813,-124,-421,578,724,960,519,666,210,783,-296,-364,-159,-317,527,143,-285,-64,-336,213,-377,691,-448,-80,8,357,-335,214,298,843,-19,723,424,509,487,-353,928,749,-357,250,323,477,587,763,788,543,-166,527,558,700,804,329,410,124,854,908,-372,347,698,-107,520,-237,865,921,-178,416,246,945,155,785,454,936,-345,568,-416,-384,-85,798,799,161,500,-271,279,492,-266,-11,22,511,-325,-71,281,298,563,575,29,125,-380,-483,-151,612,268,-284,76,-244,-472,302,991,-263,-429,227,729,332,985,919,324,-429,-242,343,-369,366,710,-247,521,-121,709,-478,-461,-235,468,-448,661,311,-291,-114,544,813,-3,167,784,-38,782,-359,844,-129,56,0,25,602,-499,679,-33,210,299,921,87,-402,413,-311,813,169,97,-319,761,170,630,968,187,101,813,-449,640,437,147,-316,-451,-116,-41,450,513,223,974,401,121,513,-486,729,-481,674,348,246,28,-207,-410,851,722,495,-419,955,-37,-202,-323,850,612,661,-171,558,981,67,87,522,-136,827,340,-313,432,-482,768,743,334,423,-9,545,920,-136,93,379,420,889,630,531,993,730,-31,339,456,149,-219,-355,-71,73,-20,861,717,611,415,-137,52,572,-104,413,-249,319,-456,-437,-475,757,573,718,68,810,15,786,312,-436,909,-374,230,593,892,-338,287,759,364,-418,-80,41,184,252,-262,871,-16,840,-190,-188,-121,323,-150,505,842,-460,625,-305,781,-300,-11,147,-61,734,-381,575,-387,112,994,12,317,410,31,792,918,838,877,224,315,859,363,901,691,-485,-183,715,300,-358,-216,-239,916,-356,-200,476,13,777,878,-88,379,606,604,-420,79,-418,-53,319,834,-267,-482,531,377,796,-179,45,967,-197,565,178,-100,545,-46,374,836,484,102,812,915,539,530,-422,193,794,-21,210,519,68,927,-387,-283,108,-485,-281,703,-204,517,-462,121,224,574,-220,-297,752,-4,-131,-68,-109,-210,931,-324,130,937,309,-189,371,-301,-76,132,951,63,789,907,-362,-414,19,-270,-360,160,-213,777,777,205,522,703,-483,-341,67,-426,851,921,24,776,-242,148,794,-2,748,-317,-484,-144,361,8,674,-271,193,743,-475,714,661,266,655,924,828,147,869,-439,-348,194,-349,531,704,483,437,104,577,-172,-306,45,606,303,-114,-424,800,810,184,96,792,41,-79,250,155,368,-149,-234,84,-310,-52,637,680,30,163,114,949,-168,-135,753,32,155,-225,837,476,-79,877,571,-381,272,249,942,279,116,-345,-254,-253,-421,-250,267,945,96,536,779,-279,329,386,-193,106,775,291,-233,602,114,30,-134,226,-360,-155,-414,321,142,-109,612,-213,720,954,763,-178,359,-300,756,17,158,355,578,-87,82,-25,-156,661,-15,-452,344,762,-399,451,711,726,-31,-402,291,932,280,335,768,608,-360,213,167,197,90,946,-499,484,-208,390,-145,120,716,-124,339,-62,649,20,804,-347,16,222,782,234,-156,-214,434,-38,794,990,875,200,951,294,61,904,706,-169,-2,193,764,-410,291,-2,-8,746,62,-331,553,197,321,997,489,171,957,616,-444,528,-376,774,41,-237,396,305,938,112,-159,725,-57,96,-268,988,-153,147,85,-91,202,263,464,88,385,725,38,689,610,934,449,789,910,383,782,954,688,-285,945,189,988,924,985,429,-23,-5,871,863,-259,930,-106,-293,172,933,-445,463,562,669,-113,80,592,685,937,80,-19,592,868,-482,-349,352,411,645,116,400,329,95,303,-395,893,115,-118,161,660,879,684,772,981,344,508,409,375,-44]
10902
"""