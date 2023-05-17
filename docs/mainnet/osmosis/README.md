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
peers="31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
