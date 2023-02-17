# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: qsr-questnet-04 | **Latest Version Tag**: v0.0.2-alpha-11 | **Wasm**: OFF

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)




## Chain explorer
[https://explorer.kjnodes.com/quasar-testnet](https://explorer.kjnodes.com/quasar-testnet)

## Public endpoints

* api: [https://quasar-testnet.api.kjnodes.com](https://quasar-testnet.api.kjnodes.com)
* rpc: [https://quasar-testnet.rpc.kjnodes.com](https://quasar-testnet.rpc.kjnodes.com)
* grpc: [https://quasar-testnet.grpc.kjnodes.com](https://quasar-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quasar-testnet.rpc.kjnodes.com:48656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quasar-testnet.rpc.kjnodes.com:48659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar-testnet/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (33)
```bash
peers="875763b4e1c4f5c2cd9395bf45c4c63eae9aea0f@213.239.217.52:43656,3a23a31e1b57f1d631edb7e9b397fe80551cc899@15.235.49.9:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:48656,1cabd0846030da442b347bb17fe02860796d253f@49.12.123.97:16656,ead98bd83daf1c4a68b3b78a3c3cd28d0637ddcd@178.128.85.30:53656,45848bc173bddbf7c685938dfada535ee5a1895b@65.109.23.114:18256,8937bdacf1f0c8b2d1ffb4606554eaf08bd55df4@5.75.255.107:26656,41ee7632f310c035235828ce03c208dbe1e24d7d@38.146.3.204:18256,a03b3f70544b32d69f322850ad2d0047973b7358@65.109.92.240:17586,b35f3493df8c3be232fe75ef7f4d0cb9d0f59668@65.109.70.23:18256,01ea9968bcacd6276f9f01ca04907953d25c2168@173.212.222.167:31656,c7c43689fe3a74d14d8159f80d070c763cbc5a81@96.234.160.22:26656,a23f002bda10cb90fa441a9f2435802b35164441@38.146.3.203:18256,7ba6ff4db4685f5196590825ca5f1a131886811d@213.202.222.182:29656,dcf78ede935a42361895928d35119ed4789abb9c@65.109.85.225:8090,1112acc7479a8a1afb0777b0b9a39fb1f7e77abd@34.175.69.87:26656,7ef67269c8ec37ff8a538a5ae83ca670fd2da686@144.126.135.137:36656,979139a41488ea532f0929682ab99659afd5266b@213.239.207.175:43656,1608ddec15a0b46785bf864b8b9666c0421ad55f@65.21.170.3:30656,5b7f8cc1a8fd8c5bc7331b26872fceb2811325ee@65.109.89.5:37656,966acc999443bae0857604a9fce426b5e09a7409@65.108.105.48:18256,46ab1cfab36eeebc9b073612d69fee1c634b22d4@147.182.244.154:26656,eeb4f094eaa62841b4a9a73f0560d6aa1fa87482@65.108.231.124:29656,08e7f2b6dcb630cb53b907018d7e9916922ecb21@137.184.160.32:2686,7bb4b5a06aba143e60ed8b70ab40d85f0b626af1@192.241.148.214:48656,5066dbc8df3696b9ffa8d92a80a7acbbccfa7c17@165.22.111.218:53656,3f8a9c71fa1a6008e8b5e10ef949e921f92cefba@185.219.142.32:05656,ad118729e8f212a85d547a6049e29ec22e6cbef6@45.67.216.40:41256,20af0bf9bdf951201cb6edc898e7e4c14c49435a@5.9.121.55:41856,fdc1babb7ad4d97a911d32b0545220c8ceca57a8@128.199.8.206:53656,69ad6dcb2c04dfb80f5f3709bcf639bc88126312@104.198.12.220:53656,b2f0b655bcbec1dc0d2bf593d227d4c2e65441c9@38.242.230.118:14656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
