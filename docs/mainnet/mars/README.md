# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: mars-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n)

## Restake

[Restake with kjnodes](https://restake.app/mars/marsvaloper1p9t4gr40rnpdwqacxgcqp7ffrfw908nu020g4n) (every 5 minutes)
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
peers="9cb92702727bc5f3d40154e625b9553a04f4d649@65.109.104.72:18556,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000,88f8e4d74b70e18d4f3515d34701704086aa77e1@38.146.3.134:18556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,66fbae56ce70f466194883bb4962a5778916439a@185.188.250.24:45656,04c687dea43de3f30df5672b30b061789a0cf8e8@144.202.72.17:26606,89757803f40da51678451735445ad40d5b15e059@169.155.44.75:26656,f6eddb5f6ef49a1a2007e586da4755b2b2081b3d@51.89.6.150:20656,d0dbb50a474888b8bed04bf8a23ac6b8bae443ee@5.79.79.80:18095,b6939330a08264dd09d531f1695e7114e0e7076c@65.108.126.35:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
