# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/jackal](https://explorer.kjnodes.com/jackal)

## Public endpoints

* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)
* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* grpc: [https://jackal.grpc.kjnodes.com](https://jackal.grpc.kjnodes.com)

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

**live-peers** (25)
```bash
peers="ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656,4fa82212d657a171b1f4d3f21da33041f5cff9f9@65.21.88.172:31656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,1f7506f1773de3bc12642f5760e016290384a16a@89.58.32.57:37656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,42909d7aedeb0a49dd9f4be1a2ba024bdd82fea2@65.144.145.234:26656,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,e98ed884751f26b98bc32d4469efd53b3507129f@15.235.114.194:10756,709d70730cbcbefd10071d316fd099160b84aced@203.135.152.216:26656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
