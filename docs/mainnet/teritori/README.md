# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-1 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

Website: [https://teritori.com](https://teritori.com)

## Restake

[Restake with kjnodes](https://restake.app/teritori/torivaloper184ln03hkpt75uhrrr26f66kvcqvf4yn4nc2xjm) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://teritori.rpc.kjnodes.com](https://teritori.rpc.kjnodes.com)
* api: [https://teritori.api.kjnodes.com](https://teritori.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@teritori.rpc.kjnodes.com:19656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@teritori.rpc.kjnodes.com:19659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/teritori/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (9)
```
peers="88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,a7ad9ae5d3eb66fa88c7167074c394e8663383f2@95.217.121.229:11074,76ac8106e8b1169f1ef28f5c45558750db85d3dc@65.108.239.241:26656,2f93424bd346b857bd5164eaac0b2bfd5fd644c0@144.91.127.252:26656,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,e3b906fefa58783395fcf72086c698707908a558@141.95.65.26:27736,5cabaab828aea4bcc60e20c5a87b469c43023557@65.108.141.109:15656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
