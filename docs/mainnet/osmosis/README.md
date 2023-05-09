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
peers="f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,914865f0b02d76c48c5369457cf5aa4173d06ed8@54.169.236.90:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
