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
* grpc: althea-testnet.grpc.kjnodes.com:52090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:52656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:52659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (40)
```bash
peers="6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,766377592cbaae65d8e6df5120bd8b4fdfc8a372@98.63.20.2:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,c58008ffca69359b3af57914c9f97b68c343f916@95.217.58.111:28656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,4a8c845bdffc8bae0ed0e91a476bc57720adec15@65.108.206.74:26656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
