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

**live-peers** (26)
```bash
peers="a877c11ecef83401dcc96c4499874ebc3f13367b@116.202.36.240:10756,ad8afbc89ac64db1ee99fdd904cbd48876d44b7d@195.3.222.240:26256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,ff7ab7fdac43752163f141809b61c67eba837cb4@65.108.97.58:37656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,4118b172fc2a45e0335c59641fd7c2e5e5e2c53c@65.108.238.203:28656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@176.42.25.134:26656,57d82676ab660e8e4471664d7fee18e3e2e3dd19@89.58.38.59:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,4963e1c374624d2c625bdb89821ed0e7290c835b@152.32.185.156:26626,2747cd770717937021e66d3da8b730c666d74ae6@65.109.93.152:36156,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
