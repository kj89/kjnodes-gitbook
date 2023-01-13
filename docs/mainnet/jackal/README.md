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

**live-peers** (14)
```bash
peers="173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,d503248df74d9b47cdb17e50146d7fe9f7d7c7f6@113.30.189.10:26656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,f460d33619705cb145d88631115a0b5581515060@165.232.173.74:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
