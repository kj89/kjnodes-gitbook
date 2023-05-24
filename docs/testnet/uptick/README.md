# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

Uptick Network is building business-grade infrastructure and  ecosystems for non-fungible tokens (NFTs). The platform is  designed with a focus on multi-chain and cross-chain interoperability,  and includes three key components: the NFT infrastructure, an NFT  marketplace, and NFT ecosystem applications.

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.6 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: uptick-testnet.grpc.kjnodes.com:11590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:11556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:11559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (9)
```bash
peers="6a775f6034f64827a6220de07b1ad344284bbf51@194.163.155.84:46656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,07df6fd3f41c4bda761931831439ab248eb3dae4@91.223.3.190:55056,86f50af23369997882ca3988eabeba998b4f07cc@65.109.92.79:10656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
