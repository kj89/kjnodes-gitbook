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
peers="fe1604c718ab19e8763ad85ed439aad5b5162718@51.250.94.153:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11556,9b7b2fb9d1416f9feadf5a58b29de0bc150d974d@65.109.89.5:30656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,174a57a0d4b914b5a9823a5f3f47ae4b06d9809e@65.108.206.118:60956,6a775f6034f64827a6220de07b1ad344284bbf51@194.163.155.84:46656,86f50af23369997882ca3988eabeba998b4f07cc@65.109.92.79:10656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
