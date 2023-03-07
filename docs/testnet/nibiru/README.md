# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (42)
```bash
peers="8b712e5f3d2a8e6a4262b47322d2dcc55e31d574@31.220.86.128:26656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,f12efee0e62eca791b4da75ca647145d3afdf1c3@86.48.26.84:39656,3fdf53758ec1552937f76c74cc887d542e9d24a9@173.249.26.138:26656,4003c942d2fd79c1ef289673a01561681a49ec03@194.163.153.41:26656,aca40f540a1945acef75d06a58a4c185764178cb@141.95.82.222:39656,77d89a919f28122c9ceef7be1d0dc761fd35a330@20.199.10.78:26656,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,93eb5997d9e174ed623dbf19205a69140ad23389@167.99.143.153:26656,9c608bf8161152c4cdffa63585e2c79834942a88@38.242.254.65:26656,4d523009433cbd75e9074af445c65c13454359a8@45.88.223.212:26656,8d29cdc290141bc1155d1b5d3eb6ee721b881ab7@95.216.163.211:26556,0bc611c38f435f2f2b8d2377a90147564d4a80fe@185.234.69.143:26656,92351b76e1ae57ae45e31a373447b60dada03d5b@75.119.153.120:26656,f2b77362c141f846c0bd8f795895bfe60589eaa7@185.237.96.110:26656,961be0b4611c61e1ac3b275580d20ab465aea1e9@157.230.177.66:26656,f3325283731df802fd9e028188e4e4380ae3aec7@31.220.85.212:26656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,d6207476a91813659a21b5a14479015aa3b3640b@34.125.57.58:18656,4fb43c4d6bd6cf0f20781b67e437263a24e4153d@95.217.75.105:31656,49cf3a642a1a04044d3a4aaa555fa438babb698d@142.132.178.151:26656,6fefa7ece2ff81d1c228c31eda72692d9299d8bc@38.242.248.145:26656,0b370f7aaf505127be417635514d9ef31a43e9f7@178.128.53.194:26656,d0ff6780f1aab6fdda65cd7e9ce478644f14120b@95.216.143.224:26656,76b1c2293a40339e55de2675ba5d5e997a1121bf@38.242.235.224:26656,5b2d7ccdf924ff16c3d0e3b55c4547a71c99dc42@161.97.122.167:39656,224c85918ea98d62daab63ba9eceab195b676760@144.91.71.1:26656,6f29a743ad237d435aac29b62528cea01ceb3ca9@46.4.91.90:26656,4591a6d3bb34030aa3b7be72691e36eb72cd6eff@128.199.47.116:26656,71d360d7d2473f4662284fd9ddbc8d253cdf0c33@95.111.232.59:28656,229218b08fa4aa43660646d33497c2318416bc1f@38.242.254.187:26656,c76596f821c629de69796d83b61ca1d0d7cdcf9a@149.102.142.113:26656,45c330a2c3b99a9c060f6911e33bb4f5eff3a286@83.171.248.30:26656,64d2ea39df1cf635fccb17311c245b9fdc56194a@91.107.195.121:26656,2a5bb3ab2343a0a1bdf1818e56e5cb402d0d266e@185.208.206.82:26656,6b9c920759355eb6614500c10e77eb138f28ed81@64.226.76.171:26656,91d0512ebcedb3f4ab9f26ae13b67166ce7a7003@46.180.223.102:26656,4d1780c1abcd7df29391bed1f5138af88424ce22@185.182.184.194:26656,a5091d1afa277bab864a495d43226ee44f85604e@212.23.222.91:39656,6be3b4bb5e56724133a04ba979aa64cd7bc6b4fd@185.53.46.52:26656,961ae324324dcdc4231dd11fde7f0d711bd72d07@95.111.232.201:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
