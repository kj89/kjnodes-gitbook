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

**live-peers** (35)
```bash
peers="6988d595d6644fcf78d7ba45c66202ad95ef7e6b@217.76.53.103:29656,bf7547ac440b049f7f17db65ab2c54befb9182cc@65.108.238.61:14656,1e0b25de6a634b693d1812584880882f43648dae@95.217.211.81:38656,d9f8b98c0de96320b16cc696eb5adbc54b4da84c@154.38.161.212:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:48656,38cf4c8da13354be52a824a0a2d0db0f3884c312@5.9.70.180:15661,1d0ff0d005171706825a734adc4ff703c06684db@217.76.53.43:29656,a6d8904b05f95bdb111da22f5159c750efb7f04c@217.76.57.185:29656,a749e6030a57bb5e338ad900432f1971be646768@199.175.98.122:29656,cc64d5aa1843547ba91a0fdafbc7aa9affa6b6fc@178.62.34.202:29656,ad0b4874462c6631daca2db6c15fc3d83403fafd@176.124.221.179:29656,b63d8a5c9a7437301373c5d8b2162e0e464f5058@80.76.235.194:29656,c7d06d1b01396a197dde70902311c6a0d8945fe4@178.63.26.94:45656,d1b369795691c3588e7580701a0561676ec8b0d4@129.226.205.208:26656,077f56a463d08a693b7f5ba7b64243a294a7eb6a@43.156.112.248:26656,966acc999443bae0857604a9fce426b5e09a7409@65.108.105.48:18256,5d3a580811ab2f08eca27900e64f90668cbabc55@138.197.188.236:29656,28d7fe2e8ce81c289af470ddddf39aa4b16569f7@185.198.27.139:34656,fb54be9b5f140da643b452651c6f2c8005c25327@159.203.20.55:29656,d8b4928dd49cede1f4b9a3b7bd3de74b352dc124@217.76.53.53:29656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27146,1ed3b66e48d4a6a84e03cd567fb0b8114f687080@65.108.244.222:29656,bfe2fd43104cd931ddd933922af3f27e3e281b10@178.62.93.227:29656,04f01368117dfeeab80d80e0f1ba3ed444f696e9@149.102.138.86:29656,c8ddf2403b5538ba9bdc6b0419e24ca3fbbc610d@84.46.240.144:48656,36f9e579cf05f94af98b36e17be802fe51069b41@109.123.248.33:48656,c4786a31543fee37c8db63a38539be23d9bdef06@5.78.67.243:53656,f12056afa6e8bd3f3d5c58a393b80c59be952dca@143.198.213.36:29656,91e36c541582b4632bf790786b00995e373a88f7@185.215.166.142:48656,34887fa8bbfe1bd4cdafde4dc48586f291bd1bb5@202.61.194.55:26656,deb4f0cf63334cba4abf7cc491921620c1393609@65.109.165.226:26656,14e5d8d95ccf3b69ab19154ebfe11710b357d51f@43.156.98.107:26656,eeb4f094eaa62841b4a9a73f0560d6aa1fa87482@65.108.231.124:29656,57519468b451ca98e7eee3be8e398eb6e6bc2fbc@43.153.204.129:26656,cf5378f1d9d42d60fecf13f506d5c0070a8855d7@43.156.73.231:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
