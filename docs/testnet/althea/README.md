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

**live-peers** (19)
```bash
peers="ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
