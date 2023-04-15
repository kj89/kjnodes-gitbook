# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (20)
```bash
peers="eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,11e8f38e3c5601e4ab2333d5a5bbb108a39b8e1c@159.69.110.238:26656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
