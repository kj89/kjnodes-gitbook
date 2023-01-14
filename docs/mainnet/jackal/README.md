# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)
* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* grpc: https://jackal.grpc.kjnodes.com:443

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

**live-peers** (22)
```bash
peers="173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656,d503248df74d9b47cdb17e50146d7fe9f7d7c7f6@113.30.189.10:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,39b55b1c49ad0994bbead006be40d9c84b0bf2d4@78.107.253.133:28656,2747cd770717937021e66d3da8b730c666d74ae6@65.109.93.152:36156,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,e61861653d42ebe5d7bf46d4c61f3753091985cd@83.53.221.249:36656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,a6bc69cf493549ee4c05f9cb6420177231570bb1@51.77.54.5:26686,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
