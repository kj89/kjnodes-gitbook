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

**live-peers** (33)
```
peers="6085c32b26fb1baa4b16b426f5d56f2fff81cfc7@135.181.165.246:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:19656,8e9624292123624e4eddc3f43189f08a0424127e@65.108.131.62:26656,43da931d00da102c002e0a227de7258b8fb1871a@144.126.135.53:26656,26d6ee4138c7533c5541722c6e1ecc6d60d47a86@104.193.254.42:26656,0af882985f5fa2db442eda8c9cf1dbcd87865ec5@65.109.94.221:1114,ec4126b26336cd61b335345df4ff2a3fbb79338a@65.109.92.240:20026,3768b801461e9934afc8cee642f8e5c10f823348@89.245.24.94:23356,3069b058b5ed85c3cdb2cf18fb1d255d966b53af@193.149.187.8:26656,3fc92d0e47257f7bd7ba1fb7a6281b56aa245682@89.117.60.92:19656,40caa979c29a9930ea2b8a6249037924d308ae84@162.55.234.70:54256,6fb98b9e316b2900fce2fd331621460a932f4d7d@65.108.15.183:51656,e8cafb5a121c9fe322e554f5a7f489b2d25abd4c@51.159.153.113:26656,ff8f8c1b4cf70f38e1c370af05a40c1845022ae8@51.79.103.43:26656,2afdb9300c47e43e555fa572d033b2d68ac28506@65.109.70.68:26686,29b92a4020171c20fe70e5d60f9c5d07dc9f31f7@194.163.161.146:26656,14e492161cc595b9da7823c27d9e5862f9e2d2c1@173.215.85.171:20030,1f9293a286df733dac6303aad3c39240ad3b3796@178.211.139.24:46656,b52a6ec019dfa39bb052dec1406a043027e24fc8@65.144.145.234:26656,60d992aae7c708c097d41829bb3968bce16379e2@51.81.107.95:10756,57909c1d8ba9162364614b83e3d18f45487aeb44@35.221.245.192:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@95.217.89.23:30552,b906f0fdace24fb415254213644b51d4d6806d28@91.226.253.197:28756,3594b73f909a9c4b87cfe6a361ef8b2b51124dd5@65.109.69.59:15956,51eaf493facf36754411baa4f7b89355bd9cb3e7@195.201.63.87:42666,f6921fded4e203ba0cd26e4ea306983763268c3a@51.159.129.164:26656,d956d6180e96c62315a777b1a3ed8f1ebf873e80@38.242.232.202:29656,82ebb17ddac20928fb8107201dad9f5aea7f9132@198.244.200.3:26656,787a6b318ebc4167fefb1d5ef9f88af6cb5a8b29@173.212.222.167:35656,a25a3a218a699e71e2a64edaa45f457dfd8507ba@65.21.148.206:26656,5ab6437f73fe71f392d53566e037aa91087530ac@139.144.67.202:26656,28456ac1dded17760432c3f1d759c7d50ab6ed3e@51.250.83.54:26656,46b7ae20e3cc4264076a91c3601f3894a021a80d@65.108.6.45:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
