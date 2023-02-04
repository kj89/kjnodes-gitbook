# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)




## Chain explorer
[https://explorer.kjnodes.com/mars](https://explorer.kjnodes.com/mars)

## Public endpoints

* api: [https://mars.api.kjnodes.com](https://mars.api.kjnodes.com)
* rpc: [https://mars.rpc.kjnodes.com](https://mars.rpc.kjnodes.com)
* grpc: [https://mars.grpc.kjnodes.com](https://mars.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@mars.rpc.kjnodes.com:45656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@mars.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="8253a88226cb44161f0f7eddb8aa0f022a0cf861@65.108.109.240:3000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,931f46cc338f59222c22565e216a16f57bbb9782@95.217.164.44:26656,eff52a6fcf2634ce1d60c1a5d38809718e22c5d2@23.88.69.22:28766,1616af7456f519a0f2360adcad45d4bb9d39c92d@146.59.85.222:26656,c16d8f6760aa4b9a09ce4dcbd74482e80e87de84@65.108.97.58:2866,c0e6bf4193accabc14171ce163e704dcec5ea5df@51.91.215.170:36095,6685404829bcbf1b8505dfcb0600c79fde44b7bb@49.12.216.13:26656,1892755333d2cc6f7ba97bda1b1c709ad4ab69cd@50.21.173.82:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
