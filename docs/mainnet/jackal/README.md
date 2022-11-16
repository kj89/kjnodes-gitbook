# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

Website: [https://jackalprotocol.com](https://jackalprotocol.com)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```
peers="a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,aa0749284ff68c721c5cd6539c7fd04f8063f2a5@65.108.105.25:11656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@71.236.119.108:57656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,8c6eae80747ae0a45befcece5170d23f432a2fb1@51.89.224.199:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
