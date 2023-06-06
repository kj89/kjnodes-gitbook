# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:15290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:15256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:15259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (35)
```bash
peers="bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,11e8f38e3c5601e4ab2333d5a5bbb108a39b8e1c@159.69.110.238:26656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,a1c05be605625e7fd3af6b9e5c84937a48482be5@35.201.194.177:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@42.119.159.212:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
