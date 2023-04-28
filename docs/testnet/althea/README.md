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

**live-peers** (29)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,87b67a8758306c61f8bb7504a0881cc837373633@140.82.38.208:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,26e70e13195b0d04cda0fca1f7b16b8746a620ed@65.109.28.226:26656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
