# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:12990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:12956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:12959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
