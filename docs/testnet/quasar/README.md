# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: qsr-questnet-04 | **Latest Version Tag**: v0.0.2-alpha-11 | **Wasm**: ON

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

**live-peers** (38)
```bash
peers="20af0bf9bdf951201cb6edc898e7e4c14c49435a@5.9.121.55:41856,0d2f608cd0ec290432cc8d4452c1d44383c9992e@38.242.241.34:29656,74c84b8e06fc2355d44cdd67582f0b1d645b4506@65.109.90.162:15656,9c5e550669e4668e536ae3b2fb15a3e6c226fa18@65.108.199.120:61056,415b36683ccfbb1fc404a491c40779b18d4e662e@65.109.108.150:29656,ed1222a42885136032aca21578c6213d8cd0efc6@65.108.9.164:53656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:48656,38cf4c8da13354be52a824a0a2d0db0f3884c312@5.9.70.180:15661,eb99675e22ec40553b971539c38ab5dbef7ed3a1@45.32.13.168:26656,fa761618e6d06967ea3935a9ec7073290fe9d220@134.209.248.48:29656,4aea60c2647dd468a5b9ebf76d4767a690d3a2c3@212.118.53.85:29656,ad118729e8f212a85d547a6049e29ec22e6cbef6@45.67.216.40:41256,a7e925ec2c9fb97832430180c0f4836844d887fb@43.156.232.251:26656,ad055e8576fbbf2044329bc6d6d14a1e717a556f@194.163.149.37:26656,d3b5f768d77136b3612a19cfdf401be6204e23f1@176.57.68.210:34656,b33fb859b56b3e0b43f3d846fdcbfd4ee2614f33@212.23.222.58:29656,c944ff2c220d8f30a399cae9580dce8319ebf052@95.217.236.79:38656,a6d8904b05f95bdb111da22f5159c750efb7f04c@217.76.57.185:29656,5167067604a6547f135c16ff93d5ab90009b81f9@136.243.149.19:26757,a83250aa10bba0b2898a1806cdbe27e658e1ba54@95.217.216.88:38656,ffbdfbd451d35af7a557eee36829244096b66911@65.108.141.109:37656,b63d8a5c9a7437301373c5d8b2162e0e464f5058@80.76.235.194:29656,966acc999443bae0857604a9fce426b5e09a7409@65.108.105.48:18256,007a06e5df8c5d203cb88bf920b820b8c20944fa@162.19.31.150:55746,848c4e9424449137abbee1d08ac9b6c11acfb5cd@43.159.61.98:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27146,b6b9daa764d034b32e3aa9e6748fc77dff627ff1@154.53.63.63:656,1e462e5f6a64b2462dfe03c36fd2cd50c81fa82e@93.92.205.213:29656,136589c157a21094c976f67bcb76bc6327c58b93@65.108.97.58:2686,2fb5f64248a1554b504d387568f819b9c222164e@129.226.208.82:26656,6d3e547559c1d8444ee571c14f718e9d009b69e2@129.226.207.121:26656,12b362239702090dbcbd921aaab16499698956bc@43.156.242.157:26656,c9bbf53f38f77f3c50588388bc0d543d0445f82e@43.156.80.232:26656,4a2db5b6e33ea2b9476784308caa7c6a778c0401@43.156.96.161:26656,3385b5c3d43d74220971141b5f4c865c76f115e3@80.65.211.114:26656,22817c8f2da42e360d340d2bf910c648cbb31c47@161.97.79.100:56656,cefcd5ddf6fb67d8a53263a0917d4fa11693cc81@65.109.167.162:26656,eeb4f094eaa62841b4a9a73f0560d6aa1fa87482@65.108.231.124:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
