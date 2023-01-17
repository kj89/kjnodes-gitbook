# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)


## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: [https://quicksilver-testnet.grpc.kjnodes.com](https://quicksilver-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (13)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,4c24df4acfbaaf22e5f6f3c4d11ecf02e8cc343f@195.3.220.48:26656,9e0604571aa20314c2261d70b7d8823414702715@51.159.141.209:26656,3c48a780b85d248e34e63eca5d44c624f93d09d5@135.181.59.162:11156,6c31ea769b18d7b20b2d738df7778fb9fc3fc380@18.236.225.32:26656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,8099f8a7c95c1676982e1a23e8452f2b10b07415@65.108.78.107:22656,c896ef12812a82eea865111c49f226849ad077db@144.76.236.90:26656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@95.217.144.121:26656,67224ac7f52eac4db6bb0a8de0bf8fbc5e7e0069@199.204.45.23:10656,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
