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
peers="ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,a7ad9ae5d3eb66fa88c7167074c394e8663383f2@95.217.121.229:11074,c7cd979a49bb288df19db750d8d15d975380e1cf@5.9.137.184:26656,3178ac8fffd269325500c95679d58d5e8ec61746@198.244.213.94:22956,bbc594f0a8424368b869fef47a18d6e35965db2e@176.9.188.21:53656,88a407d4749e1ccbb630f98ca44f304744d97864@38.242.141.168:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,b98db7bf9182a12b6ff7b8efc9f80350ccc67045@23.88.69.167:26878,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
