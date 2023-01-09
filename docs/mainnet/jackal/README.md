# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (16)
```bash
peers="c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,ad41936e5f89b119fdaae25fef0652949770f06e@185.107.57.74:26656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,9d7ec1a92e2d947cdabca9fdc44f3e047867ff06@213.170.135.153:46656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
