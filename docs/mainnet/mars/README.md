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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:45656,76969af1bccdd4dcc511741b171c3d4ccb837ba6@146.59.85.223:18556,d10e5704f3c8e9dd6ef42445e4b88bb57d0a8289@65.108.8.247:18556,9088bab4c4afb96f624fb42ba2ebd963aa4c34a1@15.235.115.147:10004,891f4fe69d1aa23d25d123aaff2b20ac63cbb001@5.75.197.137:26650,120a44a50f702717c259319caa2447c77621865f@3.39.103.198:26656,b6c3e5ea365e43cc6b9920964a948e88adc6cf5d@141.95.33.158:26650,38edf28452ebc41f661d91b6613563c864f4c72e@35.228.114.46:26656,e37baa8dbea5676d4c7f0064c5fb5f0b45780c3a@51.81.107.95:18556,c46be592341987eae20ac681cb08d2abcc02ab9a@137.74.4.20:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
