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

**live-peers** (42)
```
peers="5a4d1a83c877dd5db378ef5f897824273c2d4beb@141.95.72.198:36656,d39fecbc409541de13fa644d90066d4dabe08262@46.138.245.164:24475,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,8c6eae80747ae0a45befcece5170d23f432a2fb1@51.89.224.199:26656,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,ad34b284f0abaca967a75db713c622b53d1fb1ef@116.203.75.59:26656,2ec46ff04ebfafc19f505feaaf00943c15bb2757@185.16.38.149:26656,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,dbbd1e102b9d0cde827cd272205fa3a2886a6b2c@5.9.147.22:21656,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,fec7f91bf278a6cfc6ee3af624be914b1648b90e@65.109.64.50:36656,a77da5b3ce86a5226bae6e7b87964dd4efe8fe46@65.21.170.3:31656,55f71e8541eb2ce4115a6e44c59c0da4cd201b64@23.88.73.211:36656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,c5b43622ecd7413dd41905f6f8f5b5befd299ced@65.109.65.210:32656,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,433e26fb4d2533d81a2016a7c9ba768dd6ad2177@65.108.194.26:60756,8be44995ab4eeafcde6e0a9e196c40d483ef6d2a@51.81.155.97:10556,d00e181b66ce25775ddf5e112ebb6ff587654833@65.144.145.234:26656,bd546c50220136bf3047da1ccefa871c2cee9234@138.201.141.76:07656,7f1c65e724df6912419805981a8ff03decad68f8@155.133.22.208:23856,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656,01aca4ff5fcbffb1b4d66ea3ecffb11e9680038c@70.71.164.192:37656,5bffef5951111a8677dbc2b2a3dca4b51885740e@142.132.170.209:26638,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,01ab8944f1d486f8b3682a457a020dd7c386cc16@185.215.166.126:26656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,e4b6f1a79ee302d64aa91980200d36b31b262816@89.245.24.74:22356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656,05ab6d764ff112666275376b3f664fc3b19d3bc3@195.201.165.123:11126,9e84b3f6a6ff30cef48c80fdbe2b727e09bc2958@167.235.98.202:37656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
