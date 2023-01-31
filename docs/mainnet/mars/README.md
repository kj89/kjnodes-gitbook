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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,750935ac3bd1fda19f5bc3783d8108c27ceb10b9@66.85.151.226:36656,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000,530b1964bc17bca6457311f1c2d5a2f3d25b297a@51.81.155.97:18556,918041a30cfbf00e3bcff76faaceb3ccc3fe5032@162.19.89.8:18556,7f4be5f7db9b920e965197b65974f0e1e64749e4@144.126.128.128:26656,0c7a6911cfa419fd32c203551ea9d69f6f6fe332@51.91.144.243:26656,4903220ef96de95b98badaa0755d60b777a75c8a@144.76.175.189:18556,e61f11c5b03400d3a99c066f951ed0888a2b64af@65.108.238.103:18556,2707fa9064faa355fc98795361c2d9a3fa7514fc@185.232.69.25:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
