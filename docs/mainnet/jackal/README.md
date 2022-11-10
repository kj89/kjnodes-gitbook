# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix

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

**live-peers** | 10
```
peers="a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,dbbd1e102b9d0cde827cd272205fa3a2886a6b2c@5.9.147.22:21656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,ad34b284f0abaca967a75db713c622b53d1fb1ef@116.203.75.59:26656,3de470ce92bece46919f05141d5935e6143b9afa@88.198.34.226:11126,8c6eae80747ae0a45befcece5170d23f432a2fb1@51.89.224.199:26656,ca22db8dc1859e6ebb463317ec44b216e3767d31@185.69.166.158:26656,d39fecbc409541de13fa644d90066d4dabe08262@46.138.245.164:24475,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
