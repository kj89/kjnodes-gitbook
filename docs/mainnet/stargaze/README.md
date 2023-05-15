# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

Stargaze is a Cosmos zone (layer 1 proof-of-stake blockchain).  It is the base layer node software for the Stargaze NFT Marketplace.

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: ON

[Website](https://www.stargaze.zone) | [Discord](https://discord.gg/stargaze) | [Twitter](https://twitter.com/stargazezone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/stargaze](https://explorer.kjnodes.com/stargaze)

## Public endpoints

* api: [https://stargaze.api.kjnodes.com](https://stargaze.api.kjnodes.com)
* rpc: [https://stargaze.rpc.kjnodes.com](https://stargaze.rpc.kjnodes.com)
* grpc: stargaze.grpc.kjnodes.com:15890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:15856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.45.253:26656,82d89abe4024c54b68b8d07887cbb7f3d0710f71@130.61.146.203:26656,bb5a32a9301b06cd4f30c0e45ca023213c95e9f6@213.133.111.71:36656,dc3037694a6bb18c1d570bb4c6278323a9286de8@5.9.48.85:36656,ff10ddf3e5853586cfeab268cbab77ccbabf6927@188.166.148.13:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,a20572bc932668cf9f66598e9adc4151949da458@65.108.128.168:26656,7ff48cc8533f31c1c14a687a0a193164dbefec38@194.163.171.38:26656,6e5e6a674f41f7b1e6515ba735fbb836c0d89849@66.172.36.140:52656,ccb1f620a420bc4c2286ad816aca5c9656869430@45.34.1.114:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
