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

**live-peers** (18)
```
peers="526d8c7c44f59be9a39d7463c576b68c0db23174@65.108.234.23:15956,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,3bd3a20d7c8a26a20927289a7a6bffecf71de53e@51.81.155.97:10856,5a98d637a16b16bf425a4a785c9d11a7d1e5b8a0@65.21.131.215:26736,9c5393bb5611f8c3aaa0abde1ce753284c1428d0@141.95.34.175:27656,fe8765a154fc336ab284f28cdabc0bcb50a7afae@95.111.252.207:19656,808437b010f4663bf007b33433262d1495b0fbfe@35.90.134.158:28656,f813a00f52de54a49aea3211b89a65ae6133eac2@88.99.167.148:26686,009e25e99e3f8fde86d283d4b8b0ce2f777cde53@138.201.8.248:53656,7e6fcddab5901d18eeda4b662a499144da397028@54.37.129.164:54256,f6921fded4e203ba0cd26e4ea306983763268c3a@51.159.129.164:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,ad95a806c87682a553725a76329646425607d79f@65.108.105.25:10856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,b52a6ec019dfa39bb052dec1406a043027e24fc8@65.144.145.234:26656,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
