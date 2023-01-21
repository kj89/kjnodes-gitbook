# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[Explorer](https://explorer.kjnodes.com/jackal)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
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

**live-peers** (21)
```bash
peers="b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,d9abd1dd5bf7c57461f0476c61e28bac879430a2@141.94.109.71:10556,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,4fa82212d657a171b1f4d3f21da33041f5cff9f9@65.21.88.172:31656,753d35e39ad1f6f2fbf0f406a0c4f2bee3c4c7d0@135.181.153.228:56656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@176.42.25.134:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
