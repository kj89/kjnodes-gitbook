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

**live-peers** (21)
```bash
peers="fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,1f7506f1773de3bc12642f5760e016290384a16a@89.58.32.57:37656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,2ec46ff04ebfafc19f505feaaf00943c15bb2757@185.16.38.149:26656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,d503248df74d9b47cdb17e50146d7fe9f7d7c7f6@113.30.189.10:26656,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@23.112.14.166:26656,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,cebe2ad7290ce193069a938910905518a37f40c0@35.242.212.157:26656,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,709d70730cbcbefd10071d316fd099160b84aced@203.135.152.216:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
