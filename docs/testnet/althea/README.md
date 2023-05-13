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

**live-peers** (34)
```bash
peers="cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,c7b642db1e41d4136d3fd36a6a505a3bcc504a2f@34.73.112.90:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
