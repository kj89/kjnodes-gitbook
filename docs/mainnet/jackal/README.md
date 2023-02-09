# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every 5 minutes)
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

**live-peers** (30)
```bash
peers="599b3440878a2074e0185b48b6d51a896642a058@65.108.70.119:26656,ff7ab7fdac43752163f141809b61c67eba837cb4@65.108.97.58:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,b08a57014e190c241bd1ef5705bfc93625742030@65.21.77.173:26656,ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,2b7f02456898efbbb9da462b9b3e80ba12ff2f7c@65.109.116.50:27656,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,3ebc427c4aea796e7eea5551e8bca74a7734fe52@65.144.145.234:26656,e98ed884751f26b98bc32d4469efd53b3507129f@15.235.114.194:10756,cebe2ad7290ce193069a938910905518a37f40c0@34.159.53.53:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,4963e1c374624d2c625bdb89821ed0e7290c835b@152.32.185.156:26626,8be44995ab4eeafcde6e0a9e196c40d483ef6d2a@51.81.155.97:10556,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,8c6eae80747ae0a45befcece5170d23f432a2fb1@51.89.224.199:26656,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
