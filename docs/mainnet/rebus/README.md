# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
